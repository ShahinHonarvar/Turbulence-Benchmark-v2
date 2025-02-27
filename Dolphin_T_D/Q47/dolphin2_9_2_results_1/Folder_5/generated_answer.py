def palindromes_of_specific_lengths(s):
    s = s[63:71].lower()
    result = set()
    for length in range(4, 6):
        for i in range(len(s) - length + 1):
            subsring = s[i:i + length]
            if subsring == subsring[::-1] and subsring.isalpha():
                result.add(subsring)
    return result