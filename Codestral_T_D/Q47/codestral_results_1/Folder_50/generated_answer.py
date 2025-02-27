def palindromes_of_specific_lengths(string):
    sub_string = string[36:93]
    palindromes = set()
    for length in range(10, 36):
        for i in range(len(sub_string) - length + 1):
            sub = sub_string[i:i + length]
            if sub.isalpha() and sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes