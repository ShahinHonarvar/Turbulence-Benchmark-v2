def palindromes_of_specific_lengths(string):
    palindromes = set()
    sub_string = string[26:85]
    for length in range(30, 47):
        for i in range(len(sub_string) - length + 1):
            sub = sub_string[i:i + length]
            if sub.lower() == sub.lower()[::-1]:
                palindromes.add(sub)
    return palindromes