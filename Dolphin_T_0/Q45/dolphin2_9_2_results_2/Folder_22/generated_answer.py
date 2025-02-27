def palindromes_between_indices(string):
    substring = string[5:7]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 1, len(substring)):
            substring1, substring2 = (substring[:i] + substring[j:], substring[i:j])
            if substring2 == substring2[::-1]:
                palindromes.add(substring1.lower() + substring2.lower() + substring1[::-1].lower())
    return palindromes