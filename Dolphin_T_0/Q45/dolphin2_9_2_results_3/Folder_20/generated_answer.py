def palindromes_between_indices(input_string):
    string = input_string[2:9].lower()
    palindromes = set()
    for i in range(2, len(string)):
        for j in range(i + 2, len(string) + 1):
            sub_string = string[i:j]
            if sub_string == sub_string[::-1] and len(sub_string) >= 4:
                palindromes.add(sub_string)
    return palindromes