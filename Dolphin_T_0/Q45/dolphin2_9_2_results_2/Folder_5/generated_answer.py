def palindromes_between_indices(string):
    if len(string) < 9:
        return set()
    substring = string[4:9]
    palindromes = set()
    for i in range(len(substring)):
        if substring[i:i + 4] == substring[i:i + 4][::-1]:
            palindromes.add(substring[i:i + 4])
    return palindromes