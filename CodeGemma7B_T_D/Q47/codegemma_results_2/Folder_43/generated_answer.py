def palindromes_of_specific_lengths(user_string):
    target_substring = user_string[40:90]
    PalindromeSet = set()
    for length in range(23, 39):
        for start in range(len(target_substring) - length + 1):
            substring = target_substring[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                PalindromeSet.add(substring.lower())
    return PalindromeSet