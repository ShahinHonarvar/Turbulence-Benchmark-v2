def palindromes_of_specific_lengths(input_string):
    if len(input_string) <= 94 or len(input_string) < 52:
        return set()
    relevant_substring = input_string[39:95]
    palindromes_in_relevant_substring = [word for word in relevant_substring.split() if 14 <= len(word) <= 52]
    answer_set = set()
    for word in palindromes_in_relevant_substring:
        if word.lower() == word.lower()[::-1]:
            if word.isalpha():
                answer_set.add(word)
    return answer_set