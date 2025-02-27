def palindromes_of_specific_lengths(s):
    string = s[20:75]
    palindromes = set()
    for length in range(36, 43):
        for i in range(len(string) - length + 1):
            problem_check = string[i:i + length]
            problem_check_lower = problem_check.lower()
            if problem_check_lower == problem_check_lower[::-1] and problem_check_lower.isalpha():
                palindromes.add(problem_check)
    return palindromes