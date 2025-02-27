def all_left_right_truncatable_prime(t):
    x = t[50]
    primes = [2]
    case_two = [1]
    up_bound = x + 1
    left_and_right_truncatable_primes = []
    for val in range(3, up_bound, 2):
        if all((val % p > 0 for p in primes)):
            primes.append(val)
            if all((val % p > 0 for p in case_two)):
                case_two.append(val)
                temp_string = str(val)
                temp_string_left = temp_string[1:-1]
                temp_string_right = temp_string[:-1]
                while temp_string_left:
                    if temp_string_left in primes:
                        temp_string_left = temp_string_left[1:-1]
                    else:
                        break
                while temp_string_right:
                    if temp_string_right in primes:
                        temp_string_right = temp_string_right[:-1]
                    else:
                        break
                if temp_string_left == temp_string_right == '':
                    left_and_right_truncatable_primes.append(val)
    return sorted(left_and_right_truncatable_primes, reverse=True)