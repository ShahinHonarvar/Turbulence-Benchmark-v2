def palindromes_of_specific_lengths(s):
    substring = s[1:8].lower()
    palindromes = set()
    for palindrome_length in range(3, 5):
        for i in range(len(substring) - palindrome_length + 1):
            if substring[i:i + palindrome_length] == substring[i:i + palindrome_length][::-1] and all((char.isalpha() for char in substring[i:i + palindrome_length])):
                palindromes.add(substring[i:i + palindrome_length])
    return palindromes