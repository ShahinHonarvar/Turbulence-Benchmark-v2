def palindromes_of_specific_lengths(input_string):
    palindromes = set()
    for i in range(5):
        for j in range(i, i + 3):
            if j > len(input_string) - 1:
                continue
            substring = input_string[i:j + 1].lower()
            if substring == substring[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes