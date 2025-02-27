def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    length = len(input_string)
    for i in range(length):
        for j in range(i + 68, length + 1):
            substring = input_string[i:j]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes