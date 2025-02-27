def palindromes_between_indices(string):
    sub_string = string[4:8]
    sub_string = sub_string.lower()
    palindromes = set()
    for i in range(5, len(sub_string) + 1):
        for j in range(len(sub_string)):
            if len(sub_string[j:j + i]) == i and sub_string[j:j + i] == sub_string[j:j + i][::-1]:
                palindromes.add(sub_string[j:j + i])
    return palindromes