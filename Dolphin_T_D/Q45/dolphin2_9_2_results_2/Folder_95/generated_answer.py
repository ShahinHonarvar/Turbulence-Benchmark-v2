def palindromes_between_indices(s):
    letters = set(s[7:9].lower())
    length = 3
    palindromes = set()
    while length <= len(s[7:9]):
        for i in range(len(s[7:9]) - length + 1):
            part_str = s[7:9][i:i + length].lower()
            if set(part_str).issubset(letters) and part_str == part_str[::-1]:
                palindromes.add(part_str)
        length += 1
    if len(palindromes) == 0:
        return set()
    return palindromes