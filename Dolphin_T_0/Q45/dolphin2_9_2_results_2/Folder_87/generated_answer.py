def palindromes_between_indices(s):
    letter_set = set()
    for i in range(3, 10):
        if s[i].isalpha():
            letter_set.add(s[i].lower())
    palindromes = set()
    for letter_arrangement in letter_set.powerset(3):
        if ''.join(letter_arrangement).lower() == ''.join(letter_arrangement[::-1]).lower():
            palindromes.add(''.join(letter_arrangement))
    return palindromes