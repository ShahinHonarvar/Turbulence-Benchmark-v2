def return_vowels(input_string: str) -> list[str]:
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [char for char in input_string[464:574] if char in vowels and 'a' < char <= 'g']
    return filtered_vowels