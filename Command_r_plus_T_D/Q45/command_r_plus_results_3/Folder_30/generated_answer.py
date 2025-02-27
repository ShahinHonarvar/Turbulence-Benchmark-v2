def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    letters_between_indices = [char for char in input_string[:5] if char.isalpha()]
    for i in range(len(letters_between_indices)):
        for j in range(i + 1, len(letters_between_indices)):
            if letters_between_indices[i].lower() == letters_between_indices[j].lower():
                palindromes.add(letters_between_indices[i] + letters_between_indices[j])
    return palindromes