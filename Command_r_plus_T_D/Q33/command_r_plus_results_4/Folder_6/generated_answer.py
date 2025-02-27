def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    desired_vowels = [vowel for vowel in input_string[20:34] if vowel in vowels and 'U' < vowel <= 'i']
    return desired_vowels