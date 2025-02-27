def return_nth_smallest_ascii(input_string):
    character_list = list(input_string)
    filtered_characters = [character for i, character in enumerate(character_list) if 25 <= i <= 88]
    ascii_list = [(ord(character), character) for character in filtered_characters]
    sorted_list = sorted(ascii_list, key=lambda x: x[0])
    return sorted_list[10][1] if len(sorted_list) > 10 else 'No 11th smallest ASCII value character exists in the specified range'