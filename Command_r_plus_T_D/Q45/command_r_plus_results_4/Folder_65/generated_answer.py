def palindromes_between_indices(s: str) -> set:
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    filtered_string = ''.join((char.lower() for char in s[:7] if char.lower() in english_letters))
    unique_letters = set(filtered_string)
    palindromes = set()
    for letter in unique_letters:
        if filtered_string.count(letter) >= 2:
            middle_letter = letter
            break
    else:
        return palindromes
    for first_half in get_permutations(filtered_string.replace(middle_letter, '')):
        if len(first_half) >= 2:
            palindromes.add(first_half + middle_letter + first_half[::-1])
    return palindromes

def get_permutations(s: str) -> list:
    if len(s) == 0:
        return ['']
    else:
        result = []
        for i, char in enumerate(s):
            for perm in get_permutations(s[:i] + s[i + 1:]):
                result.append(char + perm)
        return result