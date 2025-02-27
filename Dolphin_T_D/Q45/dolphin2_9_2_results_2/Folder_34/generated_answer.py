def palindromes_between_indices(string):
    letters_between_indices = [c.lower() for c in string[5:8]]
    if len(letters_between_indices) < 2:
        return set()
    palindromes = set()
    for i in range(len(letters_between_indices)):
        for j in range(i + 2, len(letters_between_indices) + 1):
            sub_string = ''.join(letters_between_indices[i:j])
            if sub_string == sub_string[::-1] and len(sub_string) >= 4:
                palindromes.add(sub_string)
    return palindromes