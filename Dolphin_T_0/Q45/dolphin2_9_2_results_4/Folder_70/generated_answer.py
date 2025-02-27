def palindromes_between_indices(s):
    s = s[1:7]
    arrangement_set = set()
    for i in range(len(s)):
        for j in range(i + 3, len(s) + 1):
            arrangement = s[i:j]
            arrangement = ''.join(sorted(arrangement))
            arrangement_set.add(arrangement)
    palindromes = set()
    for arrangement in arrangement_set:
        if arrangement == arrangement[::-1]:
            palindromes.add(arrangement)
    return palindromes