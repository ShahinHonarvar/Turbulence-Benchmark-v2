def palindrome_of_length_at_least_n(value: str) -> set:
    palindromes = set()
    length = 62
    while length > 1:
        for i in range(len(value) - length + 1):
            substring = value[i:i + length]
            if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
                palindromes.add(substring)
        length -= 1
    return palindromes