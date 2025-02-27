def palindromes_between_indices(s):
    if len(s) < 9:
        return set()
    letters_in_range = s[6:9]
    possible_arrangements = set()
    for i in range(len(letters_in_range)):
        for j in range(i + 2, len(letters_in_range) + 1):
            substring = letters_in_range[i:j]
            if substring == substring[::-1]:
                possible_arrangements.add(substring.lower())
    return possible_arrangements