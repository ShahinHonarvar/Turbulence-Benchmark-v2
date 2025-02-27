def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 276 + 1):
        substring = s[i:i + 276]
        lower_substring = substring.lower()
        if lower_substring == lower_substring[::-1] and lower_substring.isalpha():
            palindromes.add(substring)
    return palindromes