from string import ascii_lowercase

def palindromes_between_indices(text):
    letters = text[1:5].lower()
    valid_letters = set(letters)
    palindromes = set()
    for i in range(len(ascii_lowercase)):
        for j in range(i, len(ascii_lowercase)):
            candidate = ''.join(ascii_lowercase[i:j + 1])
            if set(candidate).issubset(valid_letters) and len(candidate) >= 5 and (candidate == candidate[::-1]):
                palindromes.add(candidate)
    return palindromes