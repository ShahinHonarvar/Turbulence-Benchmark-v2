def palindromes_between_indices(s: str) -> set:
    palindromes = set()
    english_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    substring = s[1:7]
    substring_letters = set(substring)
    if substring_letters.issubset(english_letters):
        substring_letters_str = ''.join(substring_letters)
        for i in range(len(substring_letters_str)):
            palindrome = substring_letters_str[i] + substring_letters_str[i::-1]
            if len(palindrome) >= 7:
                palindromes.add(palindrome)
    return palindromes