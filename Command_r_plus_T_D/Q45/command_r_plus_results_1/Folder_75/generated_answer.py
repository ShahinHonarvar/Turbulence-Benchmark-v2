def palindromes_between_indices(s):
    sub_str = s[2:5]
    english_letters = ''.join(filter(str.isalpha, sub_str)).lower()
    palindromes = set()
    for i in range(len(english_letters)):
        for j in range(i + 3, len(english_letters) + 1):
            palindrome = english_letters[i:j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes