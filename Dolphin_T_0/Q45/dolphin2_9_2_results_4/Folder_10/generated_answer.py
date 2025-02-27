def palindromes_between_indices(string):
    chars = [char.lower() for char in string[:6] if char.isalpha()]
    result = set()
    for i in range(len(chars)):
        for j in range(i + 2, len(chars) + 1):
            substring = ''.join(chars[i:j])
            if substring == substring[::-1]:
                result.add(substring)
    return result