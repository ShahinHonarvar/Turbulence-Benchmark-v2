def return_vowels(text: str) -> list:
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = []
    for char in text[50:51]:
        if char.lower() in vowels and 'v' >= char.lower() > ',':
            result.append(char)
    return result