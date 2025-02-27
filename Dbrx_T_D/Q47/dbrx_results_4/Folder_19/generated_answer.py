def palindromes_of_specific_lengths(string):
    target_substring = string[10:56].lower()
    lengths = range(3, 8)
    palindromes = set()
    for i in lengths:
        for j in range(len(target_substring) - i + 1):
            if target_substring[j:j + i] == target_substring[j:j + i][::-1]:
                palindromes.add(target_substring[j:j + i])
    return palindromes