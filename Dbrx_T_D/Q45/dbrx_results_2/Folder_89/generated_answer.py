from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = {i: [] for i in range(ord('a'), ord('z') + 1)}
    for i in range(len(s)):
        if s[i].islower():
            english_letters[ord(s[i])].append(i)
    palindromes = set()
    for start in english_letters:
        for end in english_letters:
            if english_letters[start] and english_letters[end] and (max(english_letters[start]) < min(english_letters[end])):
                sub_str = s[max(english_letters[start]):min(english_letters[end]) + 1]
                for i in range(len(sub_str)):
                    for j in range(i, len(sub_str), 2):
                        if sub_str[i:j + 1] == sub_str[i:j + 1][::-1]:
                            palindromes.add(sub_str[i:j + 1].lower())
    long_palindromes = {palindrome for palindrome in palindromes if len(palindrome) >= 6}
    return long_palindromes