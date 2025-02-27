def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    s_lower = s[2:9].lower()
    letters_between_indices = set(s_lower) & english_letters
    letters_between_indices_count = len(letters_between_indices)
    palindromes = set()
    if letters_between_indices_count >= 2:
        for letter in letters_between_indices:
            if s_lower.count(letter) >= 2:
                palindromes.add(letter * 2)
    if letters_between_indices_count >= 3:
        for i in range(letters_between_indices_count):
            for j in range(i + 1, letters_between_indices_count):
                for k in range(j + 1, letters_between_indices_count):
                    palindromes.add(letters_between_indices.pop() + letters_between_indices.pop() + letters_between_indices.pop())
                    letters_between_indices.add(s_lower[s_lower.index(letters_between_indices.pop())])
                    letters_between_indices.add(s_lower[s_lower.index(letters_between_indices.pop())])
                    letters_between_indices.add(s_lower[s_lower.index(letters_between_indices.pop())])
    return palindromes