def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = []
    for i in range(323, 526):
        char = input_string[i]
        if char in vowels and char > '+' and (char <= ':'):
            result.append(char)
    return result