def palindrome_of_length_n(str):
    palindromes = set()
    for i in range(len(str) - 24):
        for j in range(i + 24, len(str)):
            substring = str[i:j + 1]
            reversed_substring = substring[::-1]
            if substring.lower() == reversed_substring.lower():
                palindromes.add(substring)
    if len(palindromes) == 0:
        return set()
    return palindromes