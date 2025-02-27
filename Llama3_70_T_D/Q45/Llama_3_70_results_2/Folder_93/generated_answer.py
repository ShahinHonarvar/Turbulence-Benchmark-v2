def palindromes_between_indices(s):
    s = s[2:8].lower()
    letters = ''.join(filter(str.isalpha, s))
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            substring = letters[i:i + length]
            for arrangement in generate_arrangements(substring):
                if arrangement == arrangement[::-1]:
                    palindromes.add(arrangement)
    return palindromes

def generate_arrangements(s):
    if len(s) == 1:
        yield s
    else:
        for i, char in enumerate(s):
            rest = s[:i] + s[i + 1:]
            for arrangement in generate_arrangements(rest):
                yield (char + arrangement)