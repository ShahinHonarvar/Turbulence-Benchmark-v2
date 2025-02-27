def palindrome_of_length_n(s):
    filtered_s = ''.join(filter(str.isalpha, s)).lower()
    n = 68
    palindromes = set()
    for i in range(len(filtered_s) - n + 1):
        substring = filtered_s[i:i + n]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes