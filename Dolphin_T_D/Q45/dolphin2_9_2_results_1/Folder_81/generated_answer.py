def palindromes_between_indices(s):
    letter = set(''.join((s[i] for i in range(7))))
    letter = set(letter & set('abcdefghijklmnopqrstuvwxyz'))
    letter = {i.lower() for i in letter}
    palindrome = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for length_palindrome in range(3, len(s) + 1):
        for sets in letter.combinations(length_palindrome):
            if is_palindrome(''.join(sorted(sets))):
                if all((i in letter for i in sets)):
                    palindrome.add(''.join(sorted(sets)).lower())
    return palindrome