def palindromes_between_indices(input_string):
    substring = input_string[2:6]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, len(substring) + 1):
            sub_string = substring[i:j]
            if sub_string == sub_string[::-1]:
                palindromes.add(sub_string.lower())
    return palindromes