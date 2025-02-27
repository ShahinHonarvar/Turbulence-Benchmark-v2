def find_subset_of_length_n(a):
    """The mathematical formula for the number of combinations of n elements taken r at a time is Cn(n,r)

  where n = the total number of elements in a set
        r = the number of elements chosen at a time

  Can also be calculated as:

        Cn(n,r) = n! / (r!(n-r)!)

  -- Using the formula for calculating number of subsets of length N from total length of set size N
  When N = total length of set (n = |a|) and r = size of subset (r = 60)

        C60(n,60) = n! / (60!(n-60)!)

  For this we need to import the math module which has a factorial function as it calculates the factorial of a number
  can use the following formula to calculate the desired result 
  C60(n,60) = math.factorial(n) / (math.factorial(60) * math.factorial(n - 60))

  Also, we need to use the len function from the built-in modules to calculate the size of the parameter passed to the function as it will be the value of n in the formula"""
    print(math.factorial(len(a)) / (math.factorial(60) * math.factorial(len(a) - 60)))