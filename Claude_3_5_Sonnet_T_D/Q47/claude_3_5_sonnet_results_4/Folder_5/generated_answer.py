def palindromes_of_specific_lengths(s):
    substring = s[63:71].lower()
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 4, i + 6):
            if j <= len(substring):
                potential = substring[i:j]
                if potential.isalpha() and potential == potential[::-1]:
                    palindromes.add(potential)
    return palindromes