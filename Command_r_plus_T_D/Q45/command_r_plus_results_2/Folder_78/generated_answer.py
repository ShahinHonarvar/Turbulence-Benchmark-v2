def palindromes_between_indices(s):
    sub_str = s[6:9]
    english_letters = [char for char in sub_str if char.isalpha()]
    english_letters_lower = [char.lower() for char in english_letters]
    arrangements = set()
    for i in range(3):
        for char in english_letters_lower:
            arrangements.add(char)
            if i < 2:
                for j in range(i + 1, 3):
                    arrangements.add(char + english_letters_lower[j])
    palindromes = set((arr for arr in arrangements if arr == arr[::-1]))
    return palindromes