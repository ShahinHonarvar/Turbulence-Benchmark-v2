def palindrome_of_length_at_least_n(text):
    long_polindromes = set()
    for start in range(len(text)):
        for end in range(start + 114, len(text)):
            substring = text[start:end + 1]
            if substring == substring[::-1] and substring.isalpha():
                long_polindromes.add(substring)
    return long_polindromes