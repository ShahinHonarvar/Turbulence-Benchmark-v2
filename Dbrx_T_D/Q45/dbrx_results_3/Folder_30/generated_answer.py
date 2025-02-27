from collections import defaultdict

def palindromes_between_indices(s):
    english_letters = defaultdict(set)
    for i in range(len(s)):
        if s[i].isalpha():
            english_letters[s[i].lower()].add(i)
    palindromes = set()
    for start in english_letters['a'] & english_letters['e'] & english_letters['i'] & english_letters['o'] & english_letters['u']:
        for end in english_letters['a'] & english_letters['e'] & english_letters['i'] & english_letters['o'] & english_letters['u']:
            if start > end:
                continue
            palindromes.add(s[start:end + 1])
    return {palindrome for palindrome in palindromes if len(palindrome) >= 4 and palindrome == palindrome[::-1]}