def palindromes_between_indices(s):
    english_letters = set('abcdefghijklmnopqrstuvwxyz')

    def is_palindrome(word):
        return word == word[::-1]

    def rearrange_letters(current_set):
        """
                Checks if a set of letters can be rearranged to form a palindrome.
                """
        current_set = list(current_set)
        current_set.sort()
        return is_palindrome(''.join(current_set))
    current_set = set()
    for char in s[2:9]:
        if char.lower() in english_letters:
            current_set.add(char.lower())
    if not rearrange_letters(current_set):
        return set()
    permutations = [''.join(p) for p in itertools.permutations(current_set)]
    palindromes = [p for p in permutations if is_palindrome(p)]
    palindromes = [p for p in palindromes if len(p) >= 6]
    return set(palindromes)