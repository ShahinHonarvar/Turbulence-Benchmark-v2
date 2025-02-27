def palindromes_of_specific_lengths(s):
    substring = s[0:6]
    palindrome_set = set()
    for length in range(3, 6):
        for i in range(len(substring) - (length - 1)):
            substring_to_check = substring[i:i + length]
            if substring_to_check == substring_to_check[::-1] and substring_to_check.isalpha():
                palindrome_set.add(substring_to_check.lower())
    return palindrome_set