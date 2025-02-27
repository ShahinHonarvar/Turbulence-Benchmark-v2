def if_contains_anagrams(string_list):
    """
    Count the number of anagram pairs in the list.
    """
    anagram_pairs = 0
    for string in string_list:
        if len(string) < 3:
            continue
        character_counts = {}
        for character in string.lower():
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1
        for character, count in character_counts.items():
            if count > 1:
                anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 58