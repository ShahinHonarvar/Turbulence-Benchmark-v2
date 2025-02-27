def palindromes_between_indices(input_string):
    substring = input_string[6:9]
    substring = ''.join(sorted(substring.lower()))
    palindromes = set()
    for i in range(3, len(substring) + 1):
        for j in range(i):
            if substring[j:j + i] == substring[j + i - 1::-1]:
                palindromes.add(substring[j:j + i])
    return palindromes