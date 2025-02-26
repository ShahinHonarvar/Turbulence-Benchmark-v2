def palindromes_of_specific_lengths(s):
    substr = s[200:301]
    result = set()
    for i in range(len(substr)):
        for j in range(i + 10, min(i + 51, len(substr) + 1)):
            potential = substr[i:j]
            if potential.isalpha() and potential.lower() == potential.lower()[::-1]:
                result.add(potential)
    return result