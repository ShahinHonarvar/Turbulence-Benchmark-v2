def if_contains_anagrams(input_list):
    """
            Write a function called 'if_contains_anagrams' that takes one argument, a list of strings.
            The function should return true if there are at least 25 pairs of anagrams in the given list; otherwise, it should return false.
            The function should only consider the anagrams of the length of at least three.
            The function should compare the strings in a case-insensitive manner.
            """
    all_words = [word.lower() for word in input_list]
    anagrams = []
    for i in range(len(all_words)):
        for j in range(i + 1, len(all_words)):
            if len(all_words[i]) >= 3 and len(all_words[j]) >= 3 and (sorted(all_words[i]) == sorted(all_words[j])):
                anagrams.append((i, j))
    if len(anagrams) >= 25:
        return True
    else:
        return False