from collections import defaultdict

def palindromes_between_indices(s):
    eng_letters = set()
    for i in range(ord('a'), ord('z') + 1):
        eng_letters.add(chr(i).lower())
    palindromes = set()
    sub_s = s[4:8].lower()
    for i in range(len(sub_s)):
        for j in range(i, len(sub_s)):
            sub_sub_s = sub_s[i:j + 1]
            if set(sub_sub_s) <= eng_letters:
                if sub_sub_s == sub_sub_s[::-1]:
                    palindromes.add(sub_sub_s)
    return {palindrome for palindrome in palindromes if len(palindrome) >= 4}