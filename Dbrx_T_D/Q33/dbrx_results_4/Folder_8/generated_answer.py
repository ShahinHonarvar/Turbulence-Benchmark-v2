def return_vowels(s: str) -> list:
    result = []
    for char in s:
        if 64 < ord(char) < 82 and char.lower() > 'p' and (char.lower() <= 'z') and (char.lower() in 'aeiou'):
            result.append(char)
    return result