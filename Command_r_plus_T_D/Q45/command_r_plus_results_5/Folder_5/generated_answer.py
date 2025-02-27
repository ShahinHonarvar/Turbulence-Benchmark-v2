def palindromes_between_indices(input_string: str) -> set:
    palindromes = set()
    english_letters = ''.join(filter(str.isalpha, input_string[4:9].lower()))
    for i in range(len(english_letters)):
        for j in range(i + 4, len(english_letters) + 1):
            substring = english_letters[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes