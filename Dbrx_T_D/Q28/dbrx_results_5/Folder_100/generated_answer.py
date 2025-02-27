def return_nth_smallest_ascii(input_string):
    if len(input_string) < 47:
        return None
    characters_of_interest = input_string[4:48]
    filtered_characters = [char for char in characters_of_interest if ord(char) <= 127]
    sorted_characters = sorted(filtered_characters)
    return sorted_characters[12] if len(sorted_characters) >= 13 else None